<template>
    <div>
      <input type="file" @change="handleFileUpload" ref="fileInput" />
      <button @click="submitFile">上传文件</button>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref } from 'vue';
  import { useInvoiceStore,useComponetsEvent } from '@/store';
  import http from '@/axios';
  import { ElMessage } from 'element-plus';
  
  export default defineComponent({
    setup() {
      const file = ref<File | null>(null);
      const fileInput = ref<null | HTMLInputElement>(null);
  
      const handleFileUpload = (event: Event) => {
        const input = event.target as HTMLInputElement;
        if (input.files) {
          file.value = input.files[0];
        }
      };
  
    const submitFile=async ()=> {
        if (file.value) {
          const formData = new FormData();
          formData.append('file', file.value);
          try {
            const response = await http.post('/upload', formData);
            if (response.status === 200) {
              const invoice_store = useInvoiceStore()
              invoice_store.$reset()
              invoice_store.getInvoice()
              
              ElMessage({
                message: '发票上传成功！',
                type: 'success',
                plain: true,
              });
            } else if (response.status === 201) {
              ElMessage({
                message: '没有接收到文件/没有选择文件/上传了重复的文件.',
                type: 'error',
                plain: true,
              });
            }
            // 清除文件输入
            if (fileInput.value) {
              fileInput.value.value = '';
            }
            const c_event = useComponetsEvent()
            c_event.switchUploadEvent()
  
          } catch (error) {
            console.error('上传过程中出现错误:', error);
          }
        }
      };
  
      return {
        handleFileUpload,
        submitFile,
        fileInput,
      };
    },
  });
  </script>