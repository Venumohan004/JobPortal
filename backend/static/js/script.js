// ---------------- Register ----------------

const registerForm = document.getElementById("registerForm");

if (registerForm) {

    registerForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        const user = {
            full_name: document.getElementById("full_name").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
            phone: document.getElementById("phone").value,
            role: document.getElementById("role").value
        };

        const response = await fetch("/register", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(user)
        });

        const data = await response.json();

        alert(data.message);

        if (response.ok) {
            window.location.href = "/login-page";
        }

    });

}



// ---------------- Login ----------------

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async function (e) {

        e.preventDefault();

        const user = {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value
        };

        const response = await fetch("/login", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify(user)

        });

        const data = await response.json();

        alert(data.message);

        if (response.ok) {

            localStorage.setItem("token", data.token);

            window.location.href = "/dashboard";
        }

    });

}