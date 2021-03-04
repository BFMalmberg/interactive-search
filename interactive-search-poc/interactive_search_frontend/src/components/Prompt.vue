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
        <v-col cols="12">
          <v-btn>Yes</v-btn>
        </v-col>
      </v-row>
    </v-alert>
  </div>
</template>

<script>
export default {
  name: "Prompt"
}
</script>

<style scoped>

</style>