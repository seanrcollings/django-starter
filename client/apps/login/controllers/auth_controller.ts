import { Controller } from "stimulus";

export default class extends Controller {
  static targets = ["login", "register"];
  loginTarget: HTMLElement;
  registerTarget: HTMLElement;

  initialize() {
    console.log(this.show);
    this.showTab();
  }

  showTab() {
    if (this.show === "login") {
      this.loginTarget.classList.remove("hidden");
      this.registerTarget.classList.add("hidden");
    } else if (this.show === "register") {
      this.registerTarget.classList.remove("hidden");
      this.loginTarget.classList.add("hidden");
    } else {
      console.log(":(");
    }
  }

  showRegister() {
    this.show = "register";
    this.showTab();
  }

  showLogin() {
    this.show = "login";
    this.showTab();
  }

  get show() {
    return this.data.get("show") || "";
  }

  set show(value: string) {
    this.data.set("show", value);
  }
}
