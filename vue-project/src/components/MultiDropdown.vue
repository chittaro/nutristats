<template>

    <div>
        <div @click="clicked" class = "dropdown-bar">
            <p class = "title-box"><span class = "bold">{{ title }}</span> {{ titleTrail }}</p>
            <img src = "../assets/images/arrow-down-white.png" style = "max-width: 20px;    cursor: pointer"/>
        </div>
        <div v-show = "isOpened" class = "dropdown-modal">
            <MultiDropdownItem
                title="All"
                :is-all-selected="!allSelected"
                @selected="onSelect"
                @unselected="onUnselect"
            ></MultiDropdownItem>
            <div class="divider"></div>
                
            <div v-for="item of options">
            <MultiDropdownItem
                :title="item"
                :is-all-selected="allSelected"
                @selected="onSelect"
                @unselected="onUnselect"
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
        forceClose: Boolean,
    },
    data() {
        return {
            open: false,
            allSelected: true,
            selectedItems: [],
        }
    },
    computed: {
        titleTrail() {
            if (this.selectedItems.length === 0 || 
                this.selectedItems.length === this.options.length) return ' | All'
            
            let text = ' | '
            for (let i = 0; i < this.selectedItems.length; i++){
                if (i !== 0) text += ', '
                text += this.selectedItems[i]
            }
            return text
        },
        isOpened() {
            if (this.forceClose) this.open = false
            return this.open
        }

    },
    methods: {
        clicked() {
            this.open = !this.open;
        },
        
        onSelect(item) {
            if (item === 'All'){
                this.selectedItems = [];
                this.allSelected = true;
            }
            else {
                this.allSelected = false;
                this.selectedItems.push(item);
            }
            this.$emit('change', this.selectedItems)
        },
        onUnselect(item) {
            this.selectedItems = this.selectedItems.filter(i => i !== item);
            this.$emit('change', this.selectedItems)
        },
    }
}

</script>


<style>
.dropdown-bar {
    background-color: #3C3F56;
    padding: 8px;
    border: 1px solid rgb(148, 148, 148);
    border-radius: 5px;
    width: 280px;
    cursor: pointer;
    text-overflow: clip;

    display: grid;
    grid-template-columns: 8fr 1fr;
    align-items: center;
}

.title-box {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    line-height: 1.2;
}

.dropdown-bar:hover {
    background-color: #494d69;
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