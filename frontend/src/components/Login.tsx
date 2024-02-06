import React from "react";
import { useState, useEffect } from "react";

export function Login() {
  const [user, setUser] = useState<string>();
  const [password, setPassword] = useState<string>();
  const [data, setData] = useState();

  const handleLogin = async (e) => {
    e.preventDefault();

    const res = await fetch(`http://127.0.0.1:8000/users/${user}`, { method: 'GET' });
    const data = await res.json()

    if (data.username == user && data.password == password) {
      alert("Login satisfactorio")
    } else {
      alert("Datos de login incorrectos")
    }

  }

  return (
    <div className="h-screen flex items-center justify-center font-mono">
      <div className="content-start">
        <h1 className="text-3xl">Login</h1>
      </div>
      <div>
        <div>
          <h2>User</h2>
          <input
            type="text"
            className="text-slate-900"
            onChange={(e) => setUser(e.target.value)}
          ></input>
        </div>
        <div>
          <h2>Password</h2>
          <input
            type="password"
            className="text-slate-900"
            onChange={(e) => setPassword(e.target.value)}
          ></input>
        </div>
        <button className="bg-slate-400" onClick={handleLogin}>Login</button>
      </div>
    </div>
  );
}

export default Login;
