<template>
  <v-container v-if="!error_flag">
    <v-row class="text-center" v-show="true">
      <v-col cols="12">
        <PromptBrand
            :query_string="query_string"
            :brands="brands"
            :query_results="query_results"
            @error_received="pass_on_error"
        ></PromptBrand>
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
                  v-for="result in query_results"
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

export default {
  name: "ProductResults",
  props: ['query_string', 'query_results', 'brands', 'error_flag'],
  components: {PromptBrand, Product},
  data: () => ({
    prompt_price: false,
    prompt_brand: false
  }),
  methods: {
    pass_on_error() {
      this.$emit("error_received_2", true)
    }
  }

}
</script>

<style scoped>

</style>