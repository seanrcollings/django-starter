import axios from "axios";
import Cookie from "js-cookie";

axios.defaults.headers.common["X-CSRFToken"] = Cookie.get("csrftoken");
axios.defaults.withCredentials = true;
