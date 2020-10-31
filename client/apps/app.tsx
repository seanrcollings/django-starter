import React from "react";
import ReactDom from "react-dom";
import { useGet } from "./common";

interface UserType {
  id: number;
  username: string;
  email: string;
}

function App() {
  const { data, error, loading } = useGet<UserType[]>("/api/users");

  if (loading) {
    return <div>Loading....</div>;
  }
  if (error) {
    return <div>{error.data.detail}</div>;
  }

  if (data) {
    return (
      <div>
        {data.map(user => (
          <div key={user.id}>{user.username}</div>
        ))}
      </div>
    );
  }
  return <div></div>;
}

const entry = document.getElementById("app");
ReactDom.render(<App />, entry);
