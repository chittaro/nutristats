<template>

<div class = "sort">
    <p>Sort By:</p> 
    <div class = "single-dropdown" :class="{active: open}">
        <p class = "bold" style="cursor: pointer" @click="open = !open"> {{ selected }} </p>
        <div v-if="open">
            <div class = "single-divider"></div>
            <p v-for="item of options" class = "single-option" @click = "onSelect(item)"> {{ item }} </p>
        </div>

    </div>
    <img class = "ascending-arrow" :class="{ rotated: isAscending }" @click="onRotate" src = "../assets/images/right-arrow.png"/>


</div>

</template>

<script>

export default {
    props: {
        options: Object
    },
    data() {
        return {
            selected: 'Nutrition Score',
            open: false,
            isAscending: false,
        }
    },
    methods: {
        onSelect(item) {
            this.selected = item;
            this.open = false; 
            this.$emit('selected', item);
        },
        onRotate() {
            this.isAscending = !this.isAscending;
            this.$emit('arrow', this.isAscending);
        }
    }
}

</script>

<style scoped>

.sort {
    padding: 20px 40px;
    color: #313346;

    display: flex; flex-direction: row;
    height: 30px;
    column-gap: 7px;
}

.single-dropdown {
    background-color: rgb(223, 230, 237, 0);
    padding: 8px;
    padding-top: 0px;
    border-radius: 10px;
    height: fit-content;
    z-index: 1;
}

.single-divider {
    background-color: #313346;
    height: 1px;
    margin: 8px 2px;
}

.single-option{
    border-radius: 5px;
    cursor: pointer;
}

.single-option:hover {
    background-color: #EFF7FF;
}

.active {
    background-color: rgb(201, 208, 214);
}

.ascending-arrow {
    transform: rotate(90deg);
    border-radius: 10px;
    padding: 5px;
    margin-bottom: 5px;
    max-height: 20px;
    cursor: pointer;
}

.ascending-arrow:hover {
    background-color: #EFF7FF;

}

.rotated {
    transform: rotate(-90deg);
}

</style>