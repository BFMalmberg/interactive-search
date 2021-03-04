<template>
  <div>
    <v-alert
        color="#1F22A9"
        outlined
        dense
        text
        elevation="4"
    >
      <v-row align="center">
        <v-col class="grow">
          Which brands would you like to browse?
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col v-for="option in buttons"
               :key="option.name"
               :cols="3">
          <v-btn>{{ option }}</v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </div>
</template>

<script>
export default {
  name: "Prompt",
  props: ['buttons']
}
</script>

<style scoped>

</style>