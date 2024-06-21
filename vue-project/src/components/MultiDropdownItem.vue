<template>
    <div class = "drop-item-div" @click="onClick">
        <div class="drop-outer-circ">
            <div v-if="isSelected" class="drop-inner-circ"></div>
        </div>
        <p>{{ title }}</p>
    </div>
    
</template>

<script>

export default {
    props: {
        title: String,
        isAllSelected: Boolean
    },
    data() {
        return {
            selected: false
        }
    },
    computed: {
        isSelected() {
            if (this.isAllSelected) {this.selected = false;}
            return !this.isAllSelected && this.selected;
        }
    },
    methods: {
        onClick() {

            // forced unselect OR unselect
            if (!this.isSelected){
                this.selected = true;
                this.$emit('selected', this.title);
            }

            // selected
            else {
                this.selected = false;
            }

        }
    }
}

</script>

<style>

.drop-outer-circ {
    display: flex;
    justify-content: center;
    align-items: center;

    border-radius: 50%;
    height: 20px;
    width: 20px;
    background-color: white;
}

.drop-inner-circ {
    border-radius: 50%;
    height: 12px;
    width: 12px;
    background-color: #3C3F56;
}

.drop-item-div {
    display: flex;
    flex-direction: row;
    align-items: center;

    margin: 5px;
    padding: 5px;
    cursor: pointer;
    border-radius: 10px;
}

.drop-item-div:hover {
    background-color: #494d69;
}

</style>