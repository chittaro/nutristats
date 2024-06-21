<template>

    <div>
        <div @click="clicked" class = "dropdown-bar">
            <p>{{ title }}</p>
            <img src = "../assets/images/arrow-down-white.png" style = "max-width: 20px"/>
        </div>
    
        <div v-if = "isOpened" class = "dropdown-modal">
            <MultiDropdownItem
                title="All"
                :is-all-selected="!allSelected"
                @selected="onAllSelect"
            ></MultiDropdownItem>
            <div class="divider"></div>
                
            <div v-for="item of options">
            <MultiDropdownItem
                :title="item"
                :is-all-selected="allSelected"
                @selected="onSingleSelect"
            ></MultiDropdownItem>
            </div>
        </div>

    </div>
        
</template>

<script>

import MultiDropdownItem from './MultiDropdownItem.vue'

export default {
    components: {
        MultiDropdownItem
    },
    props: {
        title: String,
        options: Object,
    },
    data() {
        return {
            isOpened: false,
            allSelected: true,
        }
    },
    methods: {
        clicked() {
            this.isOpened = !this.isOpened;
        },
        onSingleSelect() {
            this.allSelected = false;
        },
        onAllSelect() {
            this.allSelected = true;
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
    cursor: pointer;
}

.dropdown-modal{
    margin-top: 10px;
    background-color: #3C3F56;
    border-radius: 5px;
    border: 1px solid rgb(148, 148, 148);

    position: relative;
    z-index: 5;

}

.divider {
    background-color: white;
    height: 1px;
    margin: 2px 10px;
}

</style>    