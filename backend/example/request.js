const fetch = require("node-fetch");

export class Request {
    // this class lets us use GET, POST, PUT requests
    async get(url, headers={}){
        headers['Content-Type'] = 'application/json'

        const response = await fetch(url, { 
                headers:headers
            });
        
        const resData = await response.json();
        return resData; 
    }

    async post(url, data, headers={}){
        headers['Content-Type'] = 'application/json'

        const response = await fetch(url, {
            method: 'POST',
            headers:headers,
            body: JSON.stringify(data)
        });

        const resData = await response.json();
        return resData; 
    }

    async put(url, data, headers={}){
        headers['Content-Type'] = 'application/json'

        const response = await fetch(url, {
            method: 'PUT',
            headers:headers,
            body: JSON.stringify(data)
        });

        const resData = await response.json();
        return resData; 
    }

    async delete(url, headers={}){
        headers['Content-Type'] = 'application/json'

        const response = await fetch(url, {
            method: 'DELETE',
            headers:headers,
        });

        return response;
    }
}
