import axios from "axios";
import router from "./router";
import { ElMessage } from 'element-plus'



const http = axios.create({
    baseURL: 'http://127.0.0.1:5000/',
    timeout: 2 * 60 * 1000,
})

//请求拦截器
http.interceptors.request.use(
    config => {

        return config;
    },
    error => {
        console.warn(error);
        return Promise.reject(error);
    }
)

//响应拦截器
http.interceptors.response.use(
    response => {
        const res = response;
        return res;
    },
    error => {
        const res = error.response;
        if (res.status == 500) {
            ElMessage({
                message: '系统内部错误，请联系管理员',
                type: 'error',
                duration: 3 * 1000
            })
        }
        if (res.status == 404) {
            ElMessage({
                message: '未找到此资源',
                type: 'error',
                duration: 3 * 1000
            })
        }
        if (res.status == 403) {
            ElMessage({
                message: '权限不足',
                type: 'error',
                duration: 3 * 1000
            })
        }
        if (res.status == 401) {
            ElMessage({
                message: '用户未登录或Token已过期',
                type: 'error',
                duration: 3 * 1000
            })
            router.push('/')
        }
        return Promise.reject(error);
    }
)


export default http;