<template>

<div>
    <div @click="clicked" class = "dropdown-bar">
        <p>{{ title }}</p>
        <img src = "../assets/images/arrow-down.png" style = "max-width: 20px"/>
    </div>

    <div v-on-clickaway="clickAway" v-if = "isOpened" class = "dropdown-modal">
        <div v-for="item of options">
        <input type = "checkbox" id = "item" value = "item" v-model="checkedItems">
        <label for="item">{{ item }}</label>
        </div>
    </div>
</div>
    
</template>

<script>
import { directive } from "vue3-click-away" //TODO: FIX
import { sendHalls } from "../services/filter";
export default {
    props: {
        title: String,
        options: Object
    },
    directives: {
        ClickAway: directive
    },
    data() {
        return {
            isOpened: false,
        }
    },
    methods: {
        clickAway(e) {
            this.isOpened = false;
        },
        clicked(e) {
            sendHalls(this.options);
            this.isOpened = !this.isOpened;
        }
    }
}

</script>


<style>
.dropdown-bar {
    background-color: #3C3F56;
    padding: 10px;
    border: 1px solid rgb(148, 148, 148);
    border-radius: 5px;
    width: 200px;

    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    column-gap: 10px;
}

.dropdown-modal{
    margin-top: 10px;
    padding: 10px;
    background-color: #3C3F56;
    border-radius: 5px;
    border: 1px solid rgb(148, 148, 148);

}
</style>    