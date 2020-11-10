import React, { useState } from "react";
import api, { usePost } from "../../common";

export default function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const { response, execute } = usePost<api.UserType>("/api/users/", {
    username,
    password,
    email,
    firstName,
    lastName,
  });
  console.log(response);

  return (
    <div>
      <label>Username:</label>
      <input
        type='text'
        value={username}
        onChange={e => setUsername(e.target.value)}
      />
      <label>Password:</label>
      <input
        type='password'
        value={password}
        onChange={e => setPassword(e.target.value)}
      />
      <label>Email:</label>
      <input
        type='text'
        value={email}
        onChange={e => setEmail(e.target.value)}
      />
      <label>First name:</label>
      <input
        type='text'
        value={firstName}
        onChange={e => setFirstName(e.target.value)}
      />
      <label>Last Name:</label>
      <input
        type='text'
        value={lastName}
        onChange={e => setLastName(e.target.value)}
      />
      <button onClick={execute}>Submit me</button>
    </div>
  );
}
