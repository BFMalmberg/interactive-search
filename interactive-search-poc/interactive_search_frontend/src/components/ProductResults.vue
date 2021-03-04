<template>
  <v-container v-if="!error_flag">
    <v-row class="text-center" v-show="true">
      <v-col cols="12">
        <Prompt :buttons="brands"></Prompt>
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
import Prompt from "@/components/Prompt";

export default {
  name: "MapResults",
  props: ['query_results', 'brands', 'error_flag'],
  components: {Prompt, Product},
  data: () => ({
    prompt_price: false,
    prompt_brand: false
  }),


}
</script>

<style scoped>

</style>