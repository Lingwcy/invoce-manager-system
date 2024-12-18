<template>
  <el-dialog v-model="c_event.invoiceDetailEvent" title="增值税发票明细" width="800">
    <el-descriptions title="" direction="vertical" :column="4" size="Default" border>
      <el-descriptions-item label="发票代码">{{ invoice_store.selectedInvoice?.invoice_code }}</el-descriptions-item>
      <el-descriptions-item label="发票号码">{{ invoice_store.selectedInvoice?.invoice_number }}</el-descriptions-item>
      <el-descriptions-item label="开票日期">{{ invoice_store.selectedInvoice?.invoice_date }}</el-descriptions-item>
      <el-descriptions-item label="校验码">{{ invoice_store.selectedInvoice?.verification_code }}</el-descriptions-item>
      <el-descriptions-item label="购买方名称">{{ invoice_store.selectedInvoice?.buyer_name }}</el-descriptions-item>
      <el-descriptions-item label="购买方纳税人识别号">{{ invoice_store.selectedInvoice?.buyer_tax_id }}</el-descriptions-item>
      <el-descriptions-item label="税率">{{ invoice_store.selectedInvoice?.tax_rate }}</el-descriptions-item>
      <el-descriptions-item label="税额">{{ invoice_store.selectedInvoice?.tax_amount }}</el-descriptions-item>
      <el-descriptions-item label="合计">{{ invoice_store.selectedInvoice?.total_amount }}</el-descriptions-item>
      <el-descriptions-item label="销售方名称">{{ invoice_store.selectedInvoice?.seller_name }}</el-descriptions-item>
      <el-descriptions-item label="销售方开户行及账号">{{ invoice_store.selectedInvoice?.seller_bank_account }}</el-descriptions-item>
      <el-descriptions-item label="销售方纳税人识别号" :span="2">{{ invoice_store.selectedInvoice?.seller_tax_id }}</el-descriptions-item>
      <el-descriptions-item label="价税合计">{{ invoice_store.selectedInvoice?.total_tax_amount }}</el-descriptions-item>
    </el-descriptions>
  </el-dialog>
</template>

<script lang="ts" setup>
import { reactive, ref } from 'vue'
import { useComponetsEvent,useInvoiceStore } from '@/store';
const formLabelWidth = '140px'
const c_event = useComponetsEvent()
const invoice_store = useInvoiceStore()
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
const gridData = [
  {
    date: '2016-05-02',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-04',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-01',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
  {
    date: '2016-05-03',
    name: 'John Smith',
    address: 'No.1518,  Jinshajiang Road, Putuo District',
  },
]
</script>