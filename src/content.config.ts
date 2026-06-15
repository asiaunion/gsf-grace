import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const langSchema = z.enum(['ja', 'ko']).default('ja');

/** 오늘의 묵상 */
const devotionCollection = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/devotion' }),
  schema: z.object({
    title: z.string(),
    lang: langSchema,
    pubDate: z.coerce.date(),
    passage: z.string().optional(),
    draft: z.boolean().default(false),
    author: z.string().default('승주'),
  }),
});

/** 삶과 신앙 */
const faithLifeCollection = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/faith-life' }),
  schema: z.object({
    title: z.string(),
    lang: langSchema,
    pubDate: z.coerce.date(),
    description: z.string().optional(),
    draft: z.boolean().default(false),
    author: z.string().default('승주'),
  }),
});

/** 걸어가며 */
const walkCollection = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/walk' }),
  schema: z.object({
    title: z.string(),
    lang: langSchema,
    pubDate: z.coerce.date(),
    location: z.string().optional(),
    description: z.string().optional(),
    draft: z.boolean().default(false),
    author: z.string().default('승주'),
  }),
});

/** 궁금한 질문 — SEO 핵심 */
const qaCollection = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/qa' }),
  schema: z.object({
    title: z.string(),
    lang: langSchema,
    pubDate: z.coerce.date(),
    tag: z.enum([
      'suffering', 'death', 'science', 'bible', 'jesus',
      'church', 'prayer', 'salvation', 'relations', 'money', 'work',
    ]),
    question: z.string(),
    description: z.string().optional(),
    draft: z.boolean().default(false),
    author: z.string().default('승주'),
  }),
});

/** アルケ */
const archeCollection = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/arche' }),
  schema: z.object({
    title: z.string(),
    lang: langSchema,
    pubDate: z.coerce.date(),
    description: z.string().optional(),
    draft: z.boolean().default(true),
    author: z.string().default('승주'),
  }),
});

export const collections = {
  devotion: devotionCollection,
  'faith-life': faithLifeCollection,
  walk: walkCollection,
  qa: qaCollection,
  arche: archeCollection,
};
