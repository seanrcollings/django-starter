import React from "react";
import ReactDom from "react-dom";
import api from "../common";
import styled from "styled-components";

import "./styles/main.scss";

const User = styled.div`
  color: red;
`;

function App() {
  const { data, error, loading } = api.getUser(1);

  if (loading) {
    return <div>Loading....</div>;
  }
  if (error) {
    return <div>{error.data.detail}</div>;
  }

  if (data) {
    return <User>{data.username}</User>;
  }
  return <div></div>;
}

const entry = document.getElementById("app");
ReactDom.render(<App />, entry);
