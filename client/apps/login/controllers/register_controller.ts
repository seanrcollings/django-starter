import { Controller } from "stimulus";

export default class extends Controller {
  static targets = [
    "username",
    "password",
    "email",
    "firstName",
    "lastName",
    "error",
  ];
  usernameTarget: HTMLInputElement;
  passwordTarget: HTMLInputElement;
  emailTarget: HTMLInputElement;
  firstNameTarget: HTMLInputElement;
  lastNameTarget: HTMLInputElement;
  errorTarget: HTMLElement;
}
