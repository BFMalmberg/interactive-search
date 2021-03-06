<template>
  <v-container v-if="!this.backend_error_flag">
    <v-row class="text-center">
      <v-col cols="12">
        <PromptPrice v-show="prompt_price"></PromptPrice>
        <PromptBrand v-show="prompt_brand"></PromptBrand>
      </v-col>
    </v-row>
    <v-row class="text-center">
      <v-col cols="12">
        <v-card
            class="mx-auto"
        >
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
import {mapState} from "vuex";

export default {
  name: "ProductResults",
  computed: {
    ...mapState([
      'query_string',
      'query_results',
      'brands',
      'median_price',
      'show_results_flag',
      'backend_error_flag',
      'results_loading_flag',
    ]),
  },
  components: {PromptPrice, PromptBrand, Product},
  data: () => ({
    prompt_price: true,
    prompt_brand: false
  }),
  methods: {}

}
</script>

<style scoped>

</style>