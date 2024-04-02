/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry"

export class Categories extends Component {
    static template = "owl_lu.Categories";
    static props = {
        ...Component.props,
        categories: { type: Object },
    };

    setup(){
        console.log("setup");
        console.log(this.props.categories);
    }
}

registry.category("public_components").add("owl_lu.Categories", Categories);
