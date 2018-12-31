from lib.utilities import get_truncated_normal, get_truncated_exponential
from lib import static


class DistributionsManager:

    def __init__(self, yaml_parser):
        self.favorite_subjects_per_user_distribution = self.build_favorite_subjects_distribution(yaml_parser)
        self.subjects_distribution = self.build_subjects_distribution(yaml_parser)
        self.age_distribution = self.build_age_distribution(yaml_parser)

    @staticmethod
    def build_favorite_subjects_distribution(yaml_parser):
        distribution_type = yaml_parser.favorite_subjects_per_user_distribution

        if distribution_type is static.NORMAL:
            try:
                s = get_truncated_normal(yaml_parser.favorite_subjects_per_user_mean,
                                         yaml_parser.favorite_subjects_per_user_sd,
                                         yaml_parser.favorite_subjects_per_user_lower_bound,
                                         yaml_parser.favorite_subjects_per_user_upper_bound)
            except:
                print('Incorrect parameters for that kind of distribution. Using default value.')
                s = get_truncated_normal(static.NORMAL_DISTRIBUTION[1],
                                         static.NORMAL_DISTRIBUTION[2],
                                         static.NORMAL_DISTRIBUTION[3],
                                         static.NORMAL_DISTRIBUTION[4])
            return s
        else:
            try:
                s = get_truncated_exponential(yaml_parser.favorite_subjects_per_user_upper_bound,
                                              yaml_parser.favorite_subjects_per_user_lower_bound,
                                              yaml_parser.favorite_subjects_scale)
            except:
                print('Incorrect parameters for that kind of distribution. Using default value.')
                s = get_truncated_exponential(static.EXPONENTIAL_DISTRIBUTION[4],
                                              static.EXPONENTIAL_DISTRIBUTION[3],
                                              static.EXPONENTIAL_DISTRIBUTION[5])
            return s


    @staticmethod
    def build_subjects_distribution(yaml_parser):
        distribution_type = yaml_parser.subjects_distribution
        if distribution_type is static.NORMAL:
            try:
                s = get_truncated_normal(yaml_parser.subjects_mean,
                                         yaml_parser.subjects_sd,
                                         yaml_parser.subjects_lower_bound,
                                         yaml_parser.subjects_upper_bound)
            except:
                print('Incorrect parameters for that kind of distribution. Using default value.')
                s = get_truncated_normal(static.NORMAL_DISTRIBUTION[1],
                                         static.NORMAL_DISTRIBUTION[2],
                                         static.NORMAL_DISTRIBUTION[3],
                                         static.NORMAL_DISTRIBUTION[4])
            return s
        else:
            try:
                s = get_truncated_exponential(yaml_parser.subjects_upper_bound,
                                              yaml_parser.subjects_lower_bound,
                                              yaml_parser.subjects_scale)
            except:
                print('Incorrect parameters for that kind of distribution. Using default value.')
                s = get_truncated_exponential(static.EXPONENTIAL_DISTRIBUTION[4],
                                              static.EXPONENTIAL_DISTRIBUTION[3],
                                              static.EXPONENTIAL_DISTRIBUTION[5])
            return s


    @staticmethod
    def build_age_distribution(yaml_parser):
        return get_truncated_normal(yaml_parser.age_mean,
                                    yaml_parser.age_sd,
                                    yaml_parser.age_lower_bound,
                                    yaml_parser.age_upper_bound)
