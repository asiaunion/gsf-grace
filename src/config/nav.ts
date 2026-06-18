export type NavItem = {
  href: string;
  label: string;
  highlight?: boolean;
  comingSoon?: boolean;
};

export const navItemsJa: NavItem[] = [
  { href: '/story',    label: 'はじめての方へ', highlight: true },
  { href: '/qa',       label: '疑問に答える' },
  { href: '/devotion', label: 'みことば' },
  { href: '/walk',     label: '日本橋エッセイ' },
  { href: '/arche',    label: 'ἀρχή' },
];

export const navItemsKo: NavItem[] = [
  { href: '/ko/story',    label: '처음 오셨나요?', highlight: true },
  { href: '/ko/qa',       label: '궁금한 질문' },
  { href: '/ko/devotion', label: '말씀' },
  { href: '/ko/walk',     label: '니혼바시 에세이' },
  { href: '/ko/arche',    label: 'ἀρχή' },
];
