<template>

    <div class = "filter-div">
        <div class = "icon-div">
            <img src = "../assets/images/filter-icon.png" style = "max-width: 30px"/>
            <p>Filter</p>
        </div>

        <MultiDropdown 
            title = "Dining Hall"
            :options = halls
        ></MultiDropdown>

        <MultiDropdown
            title = "Meal Time"
            :options = times
        ></MultiDropdown>

        <div>
            <img src = "../assets/images/search-icon.png" style = "max-height: 50px" @click="searchRequest">
        </div>

    </div>

    <div class = "sort">
        <p>Sort By: <span class = "bold">Protein</span></p>
        <img src = "../assets/images/filled-down-icon.png" style = "max-height: 15px"/>
    </div>

</template>

<script>

import MultiDropdown from './MultiDropdown.vue'
import axios from 'axios';

export default {
    components: {
        MultiDropdown
    },
    data() {
        return {
            halls: ["Bursley", "East Quad", "Markley", "Mosher Jordan", "North Quad", "South Quad", "Twigs at Oxford"],
            times: ["Breakfast", "Lunch", "Dinner"],
            sort: 'Protein',
            
            testOutput: {}
        }
    },
    methods: {
        async searchRequest() {
                    
            const payload = { halls: this.halls, times: this.times, sort: this.sort } 
            //console.log(payload.halls)

            await axios.post('http://localhost:5001/filter', payload)
                .then((res) => { this.testOutput = res.data.data })
                .catch((error) => {console.log(error)})
            
            console.log(this.testOutput)

        }
    }
}

</script>


<style>

.filter-div {
    background-color: #313346;
    padding: 20px 40px;
    border-radius: 12px;
    color: white;
    height: 50px;
    
    display: flex;
    justify-content: flex-start;
    column-gap: 80px;
}

.icon-div {
    display: flex;
    flex-direction: row;
    column-gap: 10px;
    align-items: center;
}

.bold {
    font-family: "Inter-Regular";
}

.sort {
    padding: 20px 40px;
    color: #313346;

    display: flex; flex-direction: row;
    align-items: center;
    column-gap: 7px;
}
</style>