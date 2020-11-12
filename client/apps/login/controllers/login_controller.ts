import { Controller } from "stimulus";
import axios from "axios";
import { embededData } from "../../common/types";

export default class extends Controller {
  static targets = ["username", "password", "error"];
  usernameTarget: HTMLInputElement;
  passwordTarget: HTMLInputElement;
  errorTarget: HTMLElement;

  initialize() {
    if (embededData.user.loggedIn) {
      this.redirect();
    }
  }

  submit() {
    const username = this.usernameTarget.value;
    const password = this.passwordTarget.value;
    axios
      .post("/api/users/login/", {
        username,
        password,
      })
      .then(res => {
        console.log(res);
      })
      .catch(err => {
        console.log(err.response);
        this.errorTarget.innerHTML = err.response.data.errors.detail;
      });
  }

  redirect() {
    window.location.replace("/tests/");
  }
}
