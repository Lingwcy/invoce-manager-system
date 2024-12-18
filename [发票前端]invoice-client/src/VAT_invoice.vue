<template>
  <div id="center-box">
    <el-form :inline="true" :model="query_data" class="demo-form-inline">
      <el-form-item label="发票代码">
        <el-input v-model="query_data.invoice_code" placeholder="" clearable />
      </el-form-item>
      <el-form-item label="发票号码">
        <el-input v-model="query_data.invoice_number" placeholder="" clearable />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSearch">查询</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="c_event.switchUploadEvent()">上传</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onDownload">下载</el-button>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onPrintInvoice">打印</el-button>
      </el-form-item>
      <invoice-detail />
    </el-form>

    <el-table :data="invoice_store.invoices" style="width: 100%" ref="multipleTableRef"
      @selection-change="handleSelectionChange">
      <el-table-column type="selection" :selectable="selectable" width="55" />
      <el-table-column fixed prop="invoice_code" label="发票代码" width="150" />
      <el-table-column prop="invoice_number" label="发票号码" width="120" />
      <el-table-column prop="invoice_date" label="日期" width="140" />
      <el-table-column prop="buyer_name" label="买方名称" width="240" />
      <el-table-column prop="buyer_tax_id" label="购买方纳税人识别号" width="240" />
      <el-table-column prop="tax_rate" label="税率" width="60" />>
      <el-table-column prop="tax_amount" label="税额" width="60" />>
      <el-table-column prop="total_tax_amount" label="价税总计" width="120" />>
      <el-table-column fixed="right" label="操作" min-width="120">
        <template #default="scope">
          <el-button @click="handleClick(scope.row)">详细</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="c_event.uploadEvent" title="上传发票" width="800">
      <upload-file />
    </el-dialog>

  </div>
</template>

<script lang="ts" setup>
import print from 'print-js';
import http from './axios';
import { reactive, ref, onMounted } from 'vue'
import UploadFile from './components/UploadFile.vue';
import type { TableInstance } from 'element-plus'
import { useInvoiceStore, useComponetsEvent } from './store';
import JSZip from 'jszip';
import axios from 'axios';
import PDFMerger from 'pdf-merger-js';
import InvoiceDetail from './components/InvoiceDetail.vue';
import { ElMessage } from 'element-plus';
const c_event = useComponetsEvent()
const invoice_store = useInvoiceStore()
onMounted(() => {
  invoice_store.$reset()
  getInvoiceData().then(res => {
    const invoices: Invoice[] = JSON.parse(res);
    console.log('Invoice data received:', invoices);
    invoices.forEach(element => {
      invoice_store.invoices.push(element)
    });

  }).catch(error => {
    console.error('Error fetching invoice data:', error);
  });

})
const query_data = reactive({
  invoice_code: '',
  invoice_number: '',
})

const onSearch = async () => {
  const response = await http.get('/invoice', { params: query_data });
  const invoicesData = JSON.parse(response.data) as Invoice[];
  console.log(invoicesData)
  invoice_store.$reset()
  invoice_store.invoices.push(...invoicesData); // 使用展开运算符添加所有发票数据
  query_data.invoice_code = ''
  query_data.invoice_number = ''
}
const handleClick = (row: any) => {
  console.log(row)
  c_event.switchInvoiceDetailEvent()
  invoice_store.selectedInvoice = row as Invoice
}
const selectable = (row: Invoice) => ![1, 2].includes(row.id)
const multipleTableRef = ref<TableInstance>()
const multipleSelection = ref<Invoice[]>([])
const handleSelectionChange = (val: Invoice[]) => {
  multipleSelection.value = val
}

interface Invoice {
  id: number; // 如果id是自动生成的，前端可能不需要发送id
  invoice_code: string;
  invoice_number: string;
  invoice_date: string;
  verification_code: string;
  buyer_name: string;
  buyer_tax_id: string;
  password_zone: string;
  tax_rate: string; // 假设税率以字符串形式发送，例如 '3%'
  tax_amount: number; // 税额以元为单位
  total_amount: number; // 总金额以元为单位
  total_tax_amount: number; // 总价税额以元为单位
  seller_name: string;
  seller_tax_id: string;
  seller_address_phone: string;
  seller_bank_account: string;
  file_path: string;
}


const getInvoiceData = async (): Promise<string> => {
  try {
    const response = await http.get<string>('/invoice');
    return response.data;
  } catch (error) {
    console.error('Failed to fetch invoice data:', error);
    throw error;
  }
};

const onPrintInvoice = async () => {
  let invoice_path: string[] = multipleSelection.value.map(invoice => invoice.file_path);
  try {
    let urls = await processPrintInvoice('/download', invoice_path);
    const merger = new PDFMerger();
    // 使用Promise.all处理所有添加操作
    const addPdfPromises = urls.map((url) => {
      return merger.add(url);
    });
    await Promise.all(addPdfPromises);
    const mergedPdf = await merger.saveAsBlob();
    const mergedPdfUrl = URL.createObjectURL(mergedPdf);
    console.log(mergedPdfUrl);
    print({
      printable: mergedPdfUrl,
      type: 'pdf',
    });
    toggleSelection()
  } catch (error) {
    console.error('打印过程中发生错误:', error);
  }
};
const onDownload = async () => {
  let invoice_path: string[] = multipleSelection.value.map(invoice => invoice.file_path)
  if (invoice_path.length == 0) {
    ElMessage({
      message: '没有选择任何条目.',
      type: 'error',
      plain: true,
    });
    return
  }
  downloadFile('/download', invoice_path)
  toggleSelection()
}

const downloadService = axios.create({
  responseType: 'blob', // 指定响应数据类型为blob
  baseURL: 'http://127.0.0.1:5000/',
});

// 拿到所有发票pdf的url，推送给打印服务进行打印
const processPrintInvoice = (url: string, data?: any) => {
  return downloadService.post(url, data)
    .then(async (response) => {
      // 处理文件流
      const file = new Blob([response.data], { type: response.headers['content-type'] });
      const zip = new JSZip();
      return await zip.loadAsync(file);
    })
    .then((zip) => {
      // 遍历ZIP中的文件
      const promises: Promise<string>[] = [];
      for (const path in zip.files) {
        if (path.endsWith('.pdf')) {
          // 提取PDF文件并创建URL
          promises.push(zip.files[path].async('blob').then((pdfBlob) => {
            return URL.createObjectURL(pdfBlob);
          }));
        }
      }
      // 使用Promise.all等待所有PDF文件转换为URL
      return Promise.all(promises);
    })
    .catch((error) => {
      // 处理错误，例如提示后端返回的错误信息
      if (error.response && error.response.data) {
        const reader = new FileReader();
        reader.onload = function (event) {
          const result = reader.result;
          console.log(result); // 弹出后端返回的错误信息
        };
        reader.readAsText(error.response.data);
      }
      throw error; // 确保错误可以被外部捕获
    });
};

const downloadFile = (url: string, data?: any) => {
  return downloadService.post(url, data)
    .then((response) => {
      // 处理文件流
      const file = new Blob([response.data], { type: response.headers['content-type'] });
      const fileURL = window.URL.createObjectURL(file);
      const link = document.createElement('a');
      link.href = fileURL;
      let fileNameBase = "发票"
      const timestamp = new Date().toISOString().replace(/:|\.|\\-/g, '');
      // 创建文件名
      const fileName = `${fileNameBase}_${timestamp}.zip`;
      link.setAttribute('download', fileName); // 这里设置下载文件名
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      window.URL.revokeObjectURL(fileURL);
    })
    .catch((error) => {
      // 处理错误，例如提示后端返回的错误信息
      if (error.response && error.response.data) {
        const reader = new FileReader();
        reader.onload = function (event) {
          const result = reader.result;
          console.log(result); // 弹出后端返回的错误信息
        };
        reader.readAsText(error.response.data);
      }
    });
};


const toggleSelection = (rows?: Invoice[], ignoreSelectable?: boolean) => {
  if (rows) {
    rows.forEach((row) => {
      multipleTableRef.value!.toggleRowSelection(
        row,
        undefined,
        ignoreSelectable
      )
    })
  } else {
    multipleTableRef.value!.clearSelection()
  }
}

</script>

<style>
.demo-form-inline .el-input {
  --el-input-width: 220px;
}

.demo-form-inline .el-select {
  --el-select-width: 220px;
}

#center-box {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
</style>