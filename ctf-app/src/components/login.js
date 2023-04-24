import React, { useState } from 'react';
import axios from 'axios';
import './css/login.css';
import { useNavigate } from 'react-router-dom';

function Login() {
  // State to hold the username and password input values
  const [username, setUsername] = useState('user');
  const [password, setPassword] = useState('resu');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate()

  const handleUsernameChange = (event) => {
    setUsername(event.target.value);
  }

  const handlePasswordChange = (event) => {
    setPassword(event.target.value);
  }

  const handleLogin = async (event) => {
    event.preventDefault();

    try {
      const response = await axios.post('http://localhost:5000/login', { username, password });
      const token = response.data.access_token;
      localStorage.setItem('token', token);
      navigate('/dashboard');
    } catch (error) {
      setErrorMessage('Invalid username or password');
    }
  }

  return (
    <div className="login-container">
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <label>Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={handleUsernameChange}
        />
        <label>Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={handlePasswordChange}
        />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
