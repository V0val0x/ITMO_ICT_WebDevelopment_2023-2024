<template>
  <v-layout class="rounded rounded-md">
    <!-- Панель навигации -->
    <v-navigation-drawer permanent>
      <!-- Заголовок библиотеки -->
      <v-list-item title="Библиотека">
        <v-icon>mdi-book</v-icon>
      </v-list-item>
      <v-divider></v-divider>

      <!-- Пункты меню -->
      <template v-if="!Token.token">
        <router-link to="/login" class="text-decoration-none">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-login</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Войти</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to="/register" class="text-decoration-none">
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-account-plus</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Зарегистрироваться</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
      </template>
      <v-list-item v-else @click="Token.deleteToken" class="text-red">
        <v-list-item-icon>
          <v-icon>mdi-logout</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Выйти</v-list-item-title>
        </v-list-item-content>
      </v-list-item>

      <!-- Дополнительные пункты меню -->
      <router-link to="/categories" class="text-decoration-none">
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-format-list-bulleted</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Категории</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </router-link>
      <router-link to="/authors" class="text-decoration-none">
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-account-group</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Авторы</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </router-link>
      <router-link to="/readingrooms" class="text-decoration-none">
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-school</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Читальные залы</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </router-link>
      <router-link to="/books" class="text-decoration-none">
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-book-open</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Книги</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </router-link>
      <router-link to="/book-copies" class="text-decoration-none">
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-book-open-variant</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Экземпляры книг</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </router-link>
      <router-link to="/readers" class="text-decoration-none">
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-account</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Читатели</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </router-link>
      <router-link to="/book-takes" class="text-decoration-none">
        <v-list-item link>
          <v-list-item-icon>
            <v-icon>mdi-bookmark</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Взятые книги</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </router-link>
    </v-navigation-drawer>

    <!-- Основное содержимое -->
    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
      <router-view/>
    </v-main>
  </v-layout>
</template>


<script setup>

import {TokenStore} from "@/stores/TokenStore";

const Token = TokenStore()
</script>

<style scoped>

.text-decoration-none {
  text-decoration: none;
}

.text-red {
  color: red;
}

.v-list-item-icon {
  color: var(--color-text);
}

.v-list-item-content {
  color: var(--color-text);
}
</style>
