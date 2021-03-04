<template>
  <div>
    <v-alert
        color="#515151"
        outlined
        dense
        text
        elevation="4"
    >
      <v-row align="center">
        <v-col class="grow">
          Which brand would you like to browse further?
        </v-col>
      </v-row>
      <v-row align="center" class="justify-space-between">
        <v-col v-for="brand in this.brands"
               :key="brand"
               :cols="2">
          <v-btn color="secondary"
                 @click="brand_selected(brand)"
          >{{ brand }}
          </v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </div>
</template>

<script>
export default {
  name: "PromptPrice"
}
</script>

<style scoped>

</style>