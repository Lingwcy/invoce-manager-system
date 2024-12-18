// stores/counter.js
import { defineStore } from 'pinia'
import http from '@/axios';
interface Invoice {
  id?: number; // 如果id是自动生成的，前端可能不需要发送id
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
interface IInvoiceStore {
    invoices:Invoice[]
    selectedInvoice:Invoice | undefined
}
export const useInvoiceStore = defineStore('invoice', {
  state: (): IInvoiceStore => ({
    invoices: [],
    selectedInvoice: undefined
  }),
  actions: {
    async getInvoice() {
      try {
        const response = await http.get('/invoice');
        // 假设后端返回的是 JSON 字符串数组
        const invoicesData = JSON.parse(response.data) as Invoice[];
        this.invoices.push(...invoicesData); // 使用展开运算符添加所有发票数据
        console.log('Invoice data received:', this.invoices);
      } catch (error) {
        console.error('Failed to fetch invoice data:', error);
        throw error;
      }
    },
  },
});

export const useComponetsEvent = defineStore('cevents', {
  state: ()=> ({
    invoiceDetailEvent:false,
    uploadEvent:false
  }),
  actions: {
    switchInvoiceDetailEvent() {
      this.invoiceDetailEvent = !this.invoiceDetailEvent
    },
    switchUploadEvent(){
      this.uploadEvent = !this.uploadEvent
    }
  },
});