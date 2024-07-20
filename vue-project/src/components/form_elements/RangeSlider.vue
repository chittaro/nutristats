<template>
    <div class="slider-div">
        <input id="slider" type="text" data-slider-tooltip="hide"/>
        <p> {{rangeValues}}</p>
    </div>
</template>

<script>
import 'bootstrap-slider/dist/css/bootstrap-slider.min.css';
import Slider from 'bootstrap-slider';

export default {

    data() {
        return {
            rangeValues: [0, 100],
        }
    },
    mounted() {
        const slider = new Slider('#slider', {
            min: 0,
            max: 100,
            value: this.rangeValues,
            range: true,
            tooltip: 'always'
        });

        slider.on('change', (event) => {
            this.rangeValues = event.newValue
        });
    },
};

</script>

<style scoped>

</style>