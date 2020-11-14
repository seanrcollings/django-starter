import { Application } from "stimulus";
import { definitionsFromContext } from "stimulus/webpack-helpers";
import "../common/axiosSetup";

const application = Application.start();
const context = require.context("./controllers", true, /\.[tj]s$/);
application.load(definitionsFromContext(context));