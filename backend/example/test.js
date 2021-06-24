const fetch = require("node-fetch");
class Request {
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

        // const resData = await response.json();
        return response;
    }
}
const request = new Request()


let token = 'de73c529501624021eb410cd93cd04e180e16591';
const d = request.delete('http://127.0.0.1:8000/api/tasks/31/', {
    'Authorization': `Token ${token}`
})
d.then(e=>console.log(e))
// const a = get('http://127.0.0.1:8000/api/')
// a.then(e=>console.log(e))

// const a = request.get('http://127.0.0.1:8000/api/')
// a.then(e=>console.log(e))


// const a = get('http://127.0.0.1:8000/api/')
// a.then(e=>console.log(e))

// const b = post('http://127.0.0.1:8000/api/auth-token/', {
//     username: 'rahul',
//     password: 'vineet123',
// })
// b.then(e=>{console.log(e); token=e.token;})

// // const c = post('http://127.0.0.1:8000/api/user-register/', {
// //     username: 'rahulgupta',
// //     password: 'vineet123',
// // })
// // c.then(e=>{console.log(e)})

