import httpClient from "./httpClient";

const END_POINT = "/api/authenticate";

const validateUser = (username, password) => {
    const user = {
        "username": username,
        "password": password
    };
    return httpClient.post(END_POINT, user);
};

export {
    validateUser
}