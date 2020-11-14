import React from "react";
import ReactDom from "react-dom";

import styled from "styled-components";

import api from "../common";
import "../common/axiosSetup";
import "./styles/main.scss";

import Register from "./users/register";

const User = styled.div`
  color: white;
`;

function App() {
  const { data, error, loading } = api.getUsers();
  if (loading) {
    return <div>Loading....</div>;
  }
  if (error) {
    return <div>{error.statusText}</div>;
  }

  if (data) {
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
