import http from "../utils/http"
import {reactive, ref} from "vue"

const user = reactive({
    login_type: 0,     // 登录方式，0，密码登录，1，短信登录
    account: "",       // 登录账号/手机号/邮箱
    password: "",      // 登录密码
    remember: false,   // 是否记住登录状态
    mobile: "",        // 登录手机号码
    code: "",          // 短信验证码
    login(){
        // 用户登录
        return http.post("/users/login/", {
            "username": this.account,
            "password": this.password,
        })
    }
})

export default user;