<template>
    <FilterBlock @search="onSearch"/>
    <p class = "hint" v-if="filteredList.length === 0" style="padding-top: 60px;">press the search button to generate menu options</p>
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

<style scoped>
.items-div {
    padding: 10px 40px;

}

.hint {
    color: gray;
    text-align: center;
}

</style>