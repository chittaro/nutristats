<template>
    <div class="filter-bar">
        <div class="icon-div">
            <img src="../assets/images/filter-icon.png"/>
            <p>Filter</p>

        </div>

        <MultiDropdown 
            title="Dining Hall"
            :options=DINING_HALLS
            :forceClose="false"
        >
        </MultiDropdown>

        <div class="icon-div">
            <img src="../assets/images/utensils.png"/>
            <p>Nutrition</p>
        </div>

    </div>
</template>

<script>
import { DINING_HALLS } from '../common/constants';
import MultiDropdown from './MultiDropdown.vue';

export default {
    components: {
        MultiDropdown
    },
    data() {
        return {
            halls: DINING_HALLS,
            chosen: {
                halls: [],
            },
        }
    }
}

</script>

<style scoped>

.icon-div {
    display: flex; flex-direction: row;
    align-items: center;
    align-self: flex-start;
    gap: 10px;
    margin: 15px;
}

.icon-div img {
    max-width: 30px;
}

.filter-bar {
    background-color: #313346;
    border-radius: 20px;
    padding: 10px;
    height: 100%;
    color: white;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

</style>