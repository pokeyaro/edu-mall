import http from "../utils/http"
import {reactive, ref} from "vue"

const banner = reactive({
    banner_list: [],           // 轮播图列表
    get_banner_list(){
        return http.get("/banner/")
    },
})

export default banner;
