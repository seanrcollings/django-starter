import React from "react";
import ReactDom from "react-dom";
import api, { usePost } from "../common";
import axios from "axios";
import styled from "styled-components";
import Cookie from "js-cookie";

import "./styles/main.scss";

axios.defaults.headers.common["X-CSRFToken"] = Cookie.get("csrftoken");
axios.defaults.withCredentials = true;

const User = styled.div`
  color: white;
`;

interface Response {
  message: string;
  status: number;
}

function App() {
  const { data, error, loading } = api.getUsers();

  const handleClick = (e: Event) => {
    const instance = axios.create({
      withCredentials: true,
    });
    instance
      .post("/api/users/", { username: "tesatineaifneainf" })
      .then(result => {
        console.log(result);
      })
      .catch(err => {
        console.log(err.response);
      });
  };

  if (loading) {
    return <div>Loading....</div>;
  }
  if (error) {
    return <div>{error.data.detail}</div>;
  }

  if (data) {
    return (
      <div>
        {data.map(user => {
          return <User key={user.id}>{user.username}</User>;
        })}
        <button onClick={handleClick}>Click me</button>
      </div>
    );
  }
  return <div></div>;
}

const entry = document.getElementById("app");
ReactDom.render(<App />, entry);
