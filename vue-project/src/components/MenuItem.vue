<template>
    <div @click="isOpened = !isOpened" :class="['item-div', {isOpened: item-opened}]">
        <div class = "title-div">
            <div class = "circle-div">
                <p class = "num">{{ index + 1 }}</p>
            </div>
            <div class = "title-list-div">
                <p class="bolder"> {{ data.Menu_Item }}</p>
                <div class = "item-subdiv">
                        
                    <p> <span class = "bold">Dining Hall:</span> {{ getHall }}</p>
                    <p> <span class = "bold">Course:</span> {{ data.Course }} </p>
                    
                </div>
            </div>
        </div>

        <p>Score: <span class = "bold"> {{ data.Nutrition_Score }} </span></p>

        <img src = "../assets/images/arrow-down-blue.png" style = "max-height: 20px;"/>
    </div>
    <div v-show="isOpened" class = "details-div">
        <p>Calories: <span class = "bold"> {{ data.Calories }} </span></p>
        <p>Protein: <span class = "bold"> {{ data.Protein }}g</span></p>
        <p>Fiber: <span class = "bold"> {{ data.Dietary_Fiber }}g</span></p>
        <p>Sodium: <span class = "bold"> {{ data.Sodium }}mg</span></p>
        <p>Saturated Fat: <span class = "bold"> {{ data.Saturated_Fat }}g</span></p>
        <p>Sugar: <span class = "bold"> {{ data.Sugars }}g</span></p>
    </div>

</template>

<script>

export default {
    props: {
        data: Object,
        index: Number,
    },
    data() {
        return {
            isOpened: false,
        }
    },
    computed: {
        getHall() {
            let str = this.data.Dining_Hall
            str = str.split("-")
            for (let i = 0; i < str.length; i++){
                str[i] = str[i][0].toUpperCase() + str[i].slice(1)
            }
            return str.join(" ")

        }
    }
}

</script>

<style scoped>

.num {
    font-size: 15px;
    color: white;
    font-family: "Inter-ExtraBold";
}

.item-opened {
    background-color: red;
    border-bottom-left-radius: 0px;
    border-bottom-right-radius: 0px;
}

.circle-div {
    background-color: #3C3F56;
    border-radius: 50%;
    display: grid;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
}

.title-div {
    display: grid;
    grid-template-columns: 1fr 12fr;
    align-items: center;
    gap: 20px;
}

.item-div {
    background-color: #CFD8E1;
    border: 1px solid #3C3F56;
    border-radius: 25px;
    padding: 20px 30px;
    font-size: 25px;

    display: grid;
    grid-template-columns: 5fr 5fr 1fr;
    align-items: center;
}

.item-div:hover {
    background-color: #d9e3ee;
    cursor: pointer;
}

.title-list-div {
    display: grid;
    grid-template-rows: 1fr 1fr;
    align-items: center;
    gap: 5px;
}

.item-subdiv {
    display: grid;
    gap: 5px;
    font-size: 15px;
}

.details-div {
    background-color: #CFD8E1;
    padding: 20px;
    border-bottom-left-radius: 25px;
    border-bottom-right-radius: 25px;

    display: grid;
    grid-template-columns: 1fr 1fr;
    justify-content:space-around;
    align-items: center;
}

</style>