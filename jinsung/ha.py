from typing import List
from typing import Tuple


class JinsungHa:

    def __init__(self):
        print('About Me - Jinsung Ha')

    @property
    def workspace(self) -> Tuple[str, str]:
        company: str = 'Dable'
        position: str = 'Software Engineer'
        return company, position

    @property
    def education(self) -> str:
        degree: str = 'MEng Computing (Artificial Intelligence)'
        where: str = 'Imperial College London'
        when: str = '10.2014 - 06.2019'
        return ' | '.join([degree, where, when])
    
    @property
    def location(self) -> Tuple[float, float]:
        return 37.5665, 126.9780

    @property
    def code(self) -> List[str]:
        return [
            'Python', 'Typescript', 'Java', 'C', 'Bash'
        ]
