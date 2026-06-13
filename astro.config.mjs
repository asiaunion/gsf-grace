// @ts-check
import { defineConfig } from 'astro/config';

// NOTE: @astrojs/sitemap은 Vercel 배포 연동 시 추가 예정
// https://astro.build/config
export default defineConfig({
  site: 'https://gsfgrace.com',
  output: 'static',
  // i18n: JA first, KO secondary
  // prefixDefaultLocale: false → /ja/ 접두사 없이 일본어가 기본
  i18n: {
    defaultLocale: 'ja',
    locales: ['ja', 'ko'],
    routing: {
      prefixDefaultLocale: false,
    },
  },
});
