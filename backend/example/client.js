import {Request} from './request'

const fetch = require("node-fetch");

let token = null
const link = 'http://127.0.0.1:8000/api/'


function getAuthToken(){
    let tok = {
        'Authorization': `Token ${token}`
    }

    return tok
}

function getCreds(){
    const username = 'rahul'
    const password = 'vineet123'

    let creds = {
        username: username,
        password: password,
    }

    return creds
}
