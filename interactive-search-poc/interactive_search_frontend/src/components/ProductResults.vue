<template>
  <v-container v-if="!this.backend_error_flag">
    <v-row class="text-center" v-if="!prompt_feedback">
      <v-col cols="12" >
        <PromptPrice v-show="prompt_price"></PromptPrice>
        <PromptBrand v-show="prompt_brand"></PromptBrand>
        <PromptWeather v-show="prompt_weather" @finished="prompt_feedback = true; prompt_weather = false">
        </PromptWeather>
      </v-col>
    </v-row>
    <v-row class="text-center" v-else>
      <v-col cols="12">
        <v-card
            class="elevation-16 mx-auto"
            width="300"
        >
          <v-card-title class="headline">
            Rate Our Tool
          </v-card-title>
          <v-card-text>
            If you enjoy using Interactive Search, please take a few seconds to rate your experience with the tool.
            It really helps!

            <div class="text-center mt-12">
              <v-rating
                  v-model="rating"
                  color="#1F22A9"
                  background-color="grey darken-1"
                  empty-icon="$ratingFull"
                  half-increments
                  hover
                  large
              ></v-rating>
            </div>
          </v-card-text>
          <v-divider></v-divider>
          <v-card-actions class="justify-space-between">
            <v-btn text @click="prompt_feedback = false">
              No Thanks
            </v-btn>
            <v-btn
                color="primary"
                text
                @click="prompt_feedback = false"
            >
              Rate Now
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col cols="12">
        <div class="caption font-weight-thin" v-if="this.query_results.length > 1">
          Showing {{ this.query_results.length }} items.
        </div>
        <div class="caption font-weight-thin" v-else>
          Showing {{ this.query_results.length }} item.
        </div>
        <v-card class="mx-auto">
          <v-container fluid>
            <v-row dense>
              <v-col
                  v-for="result in this.query_results"
                  :key="result._id"
                  :cols="3"
              >
                <Product :details="result"></Product>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Product from "@/components/Product";
import PromptBrand from "@/components/PromptBrand";
import PromptPrice from "@/components/PromptPrice";
import PromptWeather from "@/components/PromptWeather";
import {mapState} from "vuex";

export default {
  name: "ProductResults",
  computed: {
    ...mapState([
      'query_string',
      'query_results',
      'brands',
      'median_price',
      'price_choice',
      'brand_choice',
      'temperature',
      'show_results_flag',
      'backend_error_flag',
      'results_loading_flag',
    ]),
  },
  components: {PromptPrice, PromptBrand, PromptWeather, Product},
  data: () => ({
    prompt_price: true,
    prompt_brand: false,
    prompt_weather: false,
    prompt_feedback: false,
    rating: null,
  }),
  watch: {
    price_choice (newVal) {
      if (newVal !== '') {
        this.prompt_price = false;
        this.prompt_brand = true;
        this.prompt_weather = false;
        this.prompt_feedback = false;
      }
    },
    brand_choice (newVal) {
      if (newVal !== '') {
        this.prompt_price = false;
        this.prompt_brand = false;
        this.prompt_weather = true;
        this.prompt_feedback = false;
      }
    }
  }

}
</script>

<style scoped>

</style>