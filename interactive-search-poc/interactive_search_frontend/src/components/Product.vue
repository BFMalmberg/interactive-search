<template>
  <v-card
      class="mx-auto"
  >
    <v-img
        :src="details['_source']['imUrl']"
        height="200px"
    ></v-img>

    <v-card-subtitle class="body-2 pl-2">
      <div class="headerClass">
        {{ details["_source"]["title"] }}
      </div>
    </v-card-subtitle>

    <v-chip
        class="ma-1"
        color="#1F22A9"
        label
        text-color="white"
    >
      <v-icon left>
        mdi-label
      </v-icon>
      EUR {{ details["_source"]["price"] }}
    </v-chip>

    <v-card-actions>
      <v-btn
          color="orange lighten-2"
          text
      >
        Explore
      </v-btn>

      <v-spacer></v-spacer>

      <v-btn
          icon
          @click="show = !show"
      >
        <v-icon>{{ show ? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show">
        <v-divider></v-divider>

        <v-card-text> {{ details["_source"]["description"] }} </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>
</template>

<script>
export default {
  name: "Product",
  props: ['details'],
  data: () => ({
    show: false,
  }),
}
</script>

<style scoped>
.headerClass{
  white-space: nowrap ;
  word-break: normal;
  overflow: hidden ;
  text-overflow: ellipsis;
  font-weight: bold;
  text-align: center;
}
</style>