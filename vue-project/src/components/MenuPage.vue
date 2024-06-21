<template>
    <FilterBlock/>
    <div class = "items-div">
        <MenuItem
            food="Chicken Parm"
            :index=1
            :score=120
        ></MenuItem>
    </div>
</template>

<script>

import FilterBlock from './FilterBlock.vue';
import MenuItem from './MenuItem.vue'

export default {
    components: {
        FilterBlock,
        MenuItem
    }
}

</script>

<style>
.items-div {
    padding: 40px;

    display: grid;
    gap: 30px;
}

</style>