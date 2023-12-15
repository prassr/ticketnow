export function validatePassword(password) {
    const regdigit=/[0-9]{1,}/
    const reglower=/[a-z]{1,}/
    const regupper=/[A-Z]{1,}/
    const reglength=/.{8,}/
    const regspecial=/[!@#$%^&*]{1,}/
    let invalid_password = false;
    let text="";
    if (!regupper.exec(password)) {
        invalid_password = true;
        text = "Must contain at least an uppercase character.";
    }
    else if (!reglower.exec(password)) {
        invalid_password = true;
        text="Must contain at least a lowercase character.";
    }
    else if (!regdigit.exec(password)) {
        invalid_password = true;
        text="Must contain at least a digit.";
    }
    else if (!reglength.exec(password)) {
        invalid_password = true;
        text = "Password length must be at least 10 characters";
    }
    else if (!regspecial.exec(password)) {
        invalid_password = true;
        text = "Must contain at least a special character from !, @, #, $, %, ^, & and *";
    }
    return {
        "invalid_password":invalid_password,
        "text": text
    }
}


export function currentDate() {
            const now = new Date();
            const year = now.getFullYear();
            let month = now.getMonth() + 1;
            let day = now.getDate();
            if (month < 10) {
                month = "0" + month;
            }
            if (day < 10) {
                day = "0" + day;
            }
            return `${year}-${month}-${day}`;
        }

export function clog(d){
    console.log(d);
}


export async function delay(n) {
    await new Promise(resolve => setTimeout(resolve, n));
// Code inside this block will be executed after waiting for 2 seconds
}

export function convertTo12HourFormat(time24) {
    const [hour, minute] = time24.split(":");
    const date = new Date(0, 0, 0, parseInt(hour), parseInt(minute));
    const options = { hour: 'numeric', minute: 'numeric', hour12: true };
    return date.toLocaleTimeString(undefined, options);
}

