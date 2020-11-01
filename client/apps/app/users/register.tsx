import React, { useState } from "react";
import api, { usePost } from "../../common";

export default function Register() {
  const [username, setUser] = useState("");
  const { state, execute } = usePost<api.UserType>("/api/users/", {
    username,
  });

  return (
    <div>
      <label>Username:</label>
      <input
        type='text'
        value={username}
        onChange={e => setUser(e.target.value)}
      />
      <button onClick={execute}>Submit me</button>
    </div>
  );
}
