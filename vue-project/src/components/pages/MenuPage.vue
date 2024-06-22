<template>
    <FilterBlock @search="onSearch"/>
    <div v-for="(item, index) of filteredList" class = "items-div">
        <MenuItem
            :data=item
            :index=index
        ></MenuItem>
    </div>
</template>

<script>

import FilterBlock from '../FilterBlock.vue';
import MenuItem from '../MenuItem.vue'

export default {
    components: {
        FilterBlock,
        MenuItem
    },

    data() {
        return {
            filteredList: []
        }
    },
    methods: {
        onSearch(data) {
            this.filteredList = data
        }
    }
}

</script>

<style>
.items-div {
    padding: 10px 40px;

}

</style>