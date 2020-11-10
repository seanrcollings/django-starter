import React, { SyntheticEvent } from "react";
import ReactDom from "react-dom";
import api, { usePost } from "../common";
import axios from "axios";
import styled from "styled-components";
import Cookie from "js-cookie";

import "./styles/main.scss";
import Register from "./users/register";

axios.defaults.headers.common["X-CSRFToken"] = Cookie.get("csrftoken");
axios.defaults.withCredentials = true;

const User = styled.div`
  color: white;
`;

function App() {
  const { data, error, loading } = api.getUsers();
  if (loading) {
    return <div>Loading....</div>;
  }
  if (error) {
    return <div>{error.data.detail}</div>;
  }

  if (data) {
    console.log(data);
    return (
      <div>
        {data.map(user => {
          return <User key={user.id}>{user.username}</User>;
        })}
        <Register />
      </div>
    );
  }
  return <div></div>;
}

const entry = document.getElementById("app");
ReactDom.render(<App />, entry);
