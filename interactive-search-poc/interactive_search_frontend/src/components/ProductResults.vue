<template>
  <v-container v-if="!error_flag">
    <v-row class="text-center" v-show="true">
      <v-col cols="12">
        <PromptBrand
            :query_string="query_string"
            :brands="brands"
            :query_results="query_results"
            @error_received="this.$emit('error_received', 'true')"
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
  name: "MapResults",
  props: ['query_string', 'query_results', 'brands', 'error_flag'],
  components: {PromptBrand, Product},
  data: () => ({
    prompt_price: false,
    prompt_brand: false
  }),


}
</script>

<style scoped>

</style>